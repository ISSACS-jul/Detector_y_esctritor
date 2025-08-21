// Este espacio esta guardado para diseñar una aplicacion la cual detecte
// el momento en el que se hace click para introducir un valor al mismo tiempo
// con la finalidad de introducir notas al sistema con mayor velocidad

#include <libinput.h>
#include <libudev.h>
#include <unistd.h>
#include <fcntl.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <errno.h>
#include <linux/input-event-codes.h>

// Funciones para abrir/cerrar dispositivos
static int open_restricted(const char *path, int flags, void *user_data) {
    int fd = open(path, flags);
    if (fd < 0)
        fprintf(stderr, "Error abriendo %s: %s\n", path, strerror(errno));
    return fd;
}

static void close_restricted(int fd, void *user_data) {
    close(fd);
}

static const struct libinput_interface interface = {
    .open_restricted = open_restricted,
    .close_restricted = close_restricted,
};

struct libinput *open_libinput_context(struct udev *udev) {
    struct libinput *li = libinput_udev_create_context(&interface, NULL, udev);
    if (!li) {
        fprintf(stderr, "No se pudo crear contexto libinput\n");
        exit(1);
    }
    if (libinput_udev_assign_seat(li, "seat0") != 0) {
        fprintf(stderr, "No se pudo asignar seat\n");
        exit(1);
    }
    return li;
}

int main(void) {
    struct udev *udev = udev_new();
    if (!udev) {
        fprintf(stderr, "No se pudo crear contexto udev\n");
        return 1;
    }

    struct libinput *li = open_libinput_context(udev);

    int fd = libinput_get_fd(li);

    while (1) {
        fd_set fds;
        FD_ZERO(&fds);
        FD_SET(fd, &fds);

        int ret = select(fd + 1, &fds, NULL, NULL, NULL);
        if (ret > 0 && FD_ISSET(fd, &fds)) {
            libinput_dispatch(li);

            struct libinput_event *event;
            while ((event = libinput_get_event(li)) != NULL) {
                if (libinput_event_get_type(event) == LIBINPUT_EVENT_POINTER_BUTTON) {
                    struct libinput_event_pointer *pointer_event =
                        libinput_event_get_pointer_event(event);

                    uint32_t button = libinput_event_pointer_get_button(pointer_event);
                    enum libinput_button_state state =
                        libinput_event_pointer_get_button_state(pointer_event);

                    if (button == BTN_LEFT && state == LIBINPUT_BUTTON_STATE_PRESSED) {
                        printf("Click izquierdo detectado!\n");
                        fflush(stdout);

                        // Ejecutar script de Python
                        system("sudo python3 input.py");

                        // Salir después de ejecutar
                        libinput_event_destroy(event);
                        libinput_unref(li);
                        udev_unref(udev);
                        return 0;
                    }
                }
                libinput_event_destroy(event);
            }
        }
    }

    libinput_unref(li);
    udev_unref(udev);
    return 0;
}

