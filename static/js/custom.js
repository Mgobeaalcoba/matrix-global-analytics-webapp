// custom.js

document.addEventListener("DOMContentLoaded", function () {
  // Event listener para el envío del formulario
  document.querySelector("form").addEventListener("submit", function (event) {
    event.preventDefault(); // Previene el envío del formulario por defecto

    // Realiza una solicitud POST al servidor
    fetch("/contacto/", {
      method: "POST",
      body: new FormData(document.querySelector("form")),
      headers: {
        "X-Requested-With": "XMLHttpRequest",
      },
    })
      .then((response) => response.json())
      .then((data) => {
        alert(data.message);
        window.location.href = "/"; // Redirecciona a la página de inicio
      });
  });
});
