/* Construyendo funciones de error y limpiar error */
function mostrarError(id, mensaje) {
    const input = document.getElementById(id);
    const error = document.getElementById(id + '-error')
    input.classList.add('is-invalid');
    error.innerText = mensaje;
}

function limpiarErrores(campos) {
    campos.forEach(campo => {
        const input = document.getElementById(campo);
        const error = document.getElementById(campo + '-error')
        input.classList.remove('is-invalid');
        error.innerText = '';
    });
}

/* Declarando errores de formulario de registro*/
const form = document.getElementById('formulario_registro');

const nombreInput = document.getElementById('nombre');
const usuarioInput = document.getElementById('usuario');
const correoInput = document.getElementById('mail');
const contrasennaInput = document.getElementById('pass');
const contrasenna2Input = document.getElementById('pass2');
const fechaInput = document.getElementById('fecha');

if (form) {
    form.addEventListener('submit', function (event) {
        event.preventDefault();
        const campos = ['nombre', 'usuario', 'mail', 'pass', 'pass2', 'fecha'];
        limpiarErrores(campos);

        let valido = true;

        if (nombreInput.value.trim() === '') {
            mostrarError('nombre', 'Por favor, ingresa un nombre válido');
            valido = false;
        }

        if (usuarioInput.value.trim() === '') {
            mostrarError('usuario', 'Por favor, ingresa un nombre de usuario válido');
            valido = false;
        }

        if (correoInput.value.trim() === '') {
            mostrarError('mail', 'Por favor, ingresa un correo válido');
            valido = false;
        } else {
            const mailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!mailRegex.test(correoInput.value)) {
                mostrarError('mail', 'El campo email debe tener un formato válido');
                valido = false;
            }
        }

        if (contrasennaInput.value === '') {
            mostrarError('pass', 'Por favor, ingresa una constraseña válida');
            valido = false;
        } else {
            const passwordRegex = /^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,18}$/;
            if (!passwordRegex.test(contrasennaInput.value)) {
                mostrarError('pass', 'La contraseña debe tener de 6 a 18 caracteres, incluir al menos una mayúscula, un número y no contener caracteres especiales');
                valido = false;
            }
        }

        if (contrasenna2Input.value !== contrasennaInput.value) {
            mostrarError('pass2', 'La constraseña debe ser igual a la anterior');
            valido = false;
        }

        if (fechaInput.value === '') {
            mostrarError('fecha', 'Por favor, ingresa una fecha válida');
            valido = false;
        } else {
            const fechaNacimiento = new Date(fechaInput.value);
            const fechaHoy = new Date();
            let edad = fechaHoy.getFullYear() - fechaNacimiento.getFullYear();
            const fechaMes = fechaHoy.getMonth() - fechaNacimiento.getMonth();
            if (fechaMes < 0 || (fechaMes === 0 && fechaHoy.getDate() < fechaNacimiento.getDate())) {
                edad--;
            }

            if (edad < 13) {
                mostrarError('fecha', 'Debes tener al menos 13 años para poder registrarte');
                valido = false;
            }
        }

        if (valido) {
            alert('¡Registrado Exitosamente!');
            form.submit();
        }
    });
}

/* Declarando errores de formulario de ingreso*/
const loginForm = document.getElementById('formulario_ingreso');

const usuarioLogin = document.getElementById('usuarioLogin');
const contrasennaLogin = document.getElementById('passLogin');


if (loginForm) {
    loginForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const campos = ['usuarioLogin', 'passLogin'];
        limpiarErrores(campos);

        let valido = true;

        if (usuarioLogin.value.trim() === '') {
            mostrarError('usuarioLogin', 'Por favor, ingresa tu nombre de usuario');
            valido = false;
        }

        if (contrasennaLogin.value.trim() === '') {
            mostrarError('passLogin', 'Por favor, ingresa tu contraseña');
            valido = false;
        }

        if (valido) {
            alert('Inicio de sesión exitoso');
        }
    })
}

/* Declarando errores de formulario recuperar contraseña*/
const mailForm = document.getElementById('formulario_email');

const verificacionEmail = document.getElementById('verificacionEmail');

if (mailForm) {
    mailForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const mail = ['verificacionEmail'];
        limpiarErrores(mail);

        let valido = true;

        if (verificacionEmail.value.trim() === '') {
            mostrarError('verificacionEmail', 'Por favor, ingresa un correo válido');
            valido = false;
        } else {
            const correoRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!correoRegex.test(verificacionEmail.value)) {
                mostrarError('verificacionEmail', 'El campo email debe tener un formato válido');
                valido = false;
            }
        }

        if (valido) {
            alert('Email correcto');
            window.location.href = '/formulario_recuperarpw.html';
        }
    })
}



/* Declarando errores de formulario nueva contraseña*/
const passForm = document.getElementById('formulario_contrasenna');

const newPass = document.getElementById('newPass');
const newPass2 = document.getElementById('newPass2')

if (passForm) {
    passForm.addEventListener('submit', function (event) {
        event.preventDefault();

        const contrasennas = ['newPass', 'newPass2'];
        limpiarErrores(contrasennas);

        let valido = true;

        if (newPass.value === '') {
            mostrarError('newPass', 'Por favor, ingresa una constraseña válida');
            valido = false;
        } else {
            const contrasennaRegex = /^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,18}$/;
            if (!contrasennaRegex.test(newPass.value)) {
                mostrarError('newPass', 'La contraseña debe tener de 6 a 18 caracteres, incluir al menos una mayúscula, un número y no contener caracteres especiales');
                valido = false;
            }
        }

        if (newPass2.value !== newPass.value) {
            mostrarError('newPass2', 'La constraseña debe ser igual a la anterior');
            valido = false;
        }

        if (valido) {
            alert('Cambio de contraseña exitoso');
        }
    })
}


/* Declarando errores de formulario de modificación*/
const formCambio = document.getElementById('formulario_modificacion');

const modifNombre = document.getElementById('modifNombre');
const modifUsuario = document.getElementById('modifUsuario');
const modifCorreo = document.getElementById('modifMail');
const modifContrasenna = document.getElementById('modifPass');
const modifContrasenna2 = document.getElementById('modifPass2');

if (formCambio) {
    formCambio.addEventListener('submit', function (event) {
        event.preventDefault();
        const modifCampos = ['modifNombre', 'modifUsuario', 'modifMail', 'modifPass', 'modifPass2'];
        limpiarErrores(modifCampos);

        let valido = true;

        if (modifNombre.value.trim() === '') {
            mostrarError('modifNombre', 'Por favor, ingresa un nombre válido');
            valido = false;
        }

        if (modifUsuario.value.trim() === '') {
            mostrarError('modifUsuario', 'Por favor, ingresa un nombre de usuario válido');
            valido = false;
        }

        if (modifCorreo.value.trim() === '') {
            mostrarError('modifMail', 'Por favor, ingresa un correo válido');
            valido = false;
        } else {
            const modifMailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (!modifMailRegex.test(modifCorreo.value)) {
                mostrarError('modifMail', 'El campo email debe tener un formato válido');
                valido = false;
            }
        }

        if (modifContrasenna.value === '') {
            mostrarError('modifPass', 'Por favor, ingresa una constraseña válida');
            valido = false;
        } else {
            const modifPasswordRegex = /^(?=.*[A-Z])(?=.*\d)[A-Za-z\d]{6,18}$/;
            if (!modifPasswordRegex.test(contrasennaInput.value)) {
                mostrarError('modifPass', 'La contraseña debe tener de 6 a 18 caracteres, incluir al menos una mayúscula, un número y no contener caracteres especiales');
                valido = false;
            }
        }

        if (modifContrasenna2.value !== contrasennaInput.value) {
            mostrarError('modifPass2', 'La constraseña debe ser igual a la anterior');
            valido = false;
        }

        if (valido) {
            alert('¡Cambios realizados Exitosamente!');
            form.submit();
        }
    });
}


/* Creando usuarios de prueba*/
const users = [
    {usuario: 'admin', contrasenna: 'admin1234', rol: 'admin'},
    {usuario: 'cliente', contrasenna: 'cliente1234', rol: 'cliente'}
];

const formLogin = document.getElementById('formulario_ingreso');

if (formLogin) {
    formLogin.addEventListener('submit', function (event) {
        event.preventDefault();

        const inputUsuario = document.getElementById('usuarioLogin').value.trim();
        const inputContrasenna = document.getElementById('passLogin').value;

        const usuarioEncontrado = users.find(u => u.usuario === inputUsuario && u.contrasenna === inputContrasenna);

        if (usuarioEncontrado) {
            localStorage.setItem('rolUsuario', usuarioEncontrado.rol);
            localStorage.setItem('nombreUsuario', usuarioEncontrado.usuario);

            window.location.href = '/index.html';
        } else {
            alert('Usuario o contraseña incorrectos');
        }
    });
}


/* Usuario logueado, se deja de mostrar botones "Inicio sesión", "Regístrate acá"
   y aparece botón "Cerrar sesión"*/
document.addEventListener('DOMContentLoaded', function() {
    const btnLogin = document.getElementById('btnLogin');
    const btnRegistrar = document.getElementById('btnRegistrar');
    const rolUsuario = localStorage.getItem('rolUsuario');
    const nombreUsuario = localStorage.getItem('nombreUsuario');
    const btnLogout = document.getElementById('btnLogout');

    if (rolUsuario && nombreUsuario) {
        btnLogin.style.display = 'none';
        btnRegistrar.style.display = 'none';
        btnLogout.classList.remove('d-none');

        btnLogout.addEventListener('click', function () {
            localStorage.removeItem('rolUsuario');
            localStorage.removeItem('nombreUsuario');
            window.location.reload();
        })
    }
})