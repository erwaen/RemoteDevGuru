import React, { useState } from "react";
import emailjs from "emailjs-com";
import Navbar from "../components/NavBar";

const Support = () => {
  const [fullName, setFullName] = useState("");
  const [email, setEmail] = useState("");
  const [message, setMessage] = useState("");
  const [isSent, setIsSent] = useState(false);

  const handleSubmit = (event) => {
    event.preventDefault();

    // Separar el nombre y el apellido
    const [name, lastName] = fullName.split(" ");

    // Configurar EmailJS
    emailjs
      .send(
        "service_6hj57kl",
        "template_4yf7zz1",
        {
          from_name: name,
          to_name: "Remote Dev Guru",
          from_email: email,
          to_email: "maurogimenezb@gmail.com",
          message: message,
        },
        "V3q9UbEYUHUMpjXC0"
      )
      .then(
        () => {
          console.log("Correo enviado correctamente");
          // Restablecer los campos del formulario
          setFullName("");
          setEmail("");
          setMessage("");
          setIsSent(true);
        },
        (error) => {
          console.error("Error al enviar el correo", error);
        }
      );
  };

  return (
    <div className="hero min-h-screen bg-base-100 fixed top-[61px] ">
      <Navbar></Navbar>
      <div className="hero-content text-center">
        <div className="max-w-md mx-auto">
          <h1 className="text-3xl md:text-5xl font-bold mb-10">Bienvenido a Soporte</h1>
          <form onSubmit={handleSubmit} className="flex flex-col gap-0.5">
            <label className="label">
              <span className="label-text">Cuál es tu nombre y apellido?</span>
            </label>
            <input
              type="text"
              placeholder="Nombre y Apellido"
              className="input input-bordered"
              value={fullName}
              onChange={(event) => setFullName(event.target.value)}
            />
            <label className="label">
              <span className="label-text">Cuál es tu correo electrónico?</span>
            </label>
            <input
              type="email"
              placeholder="Correo Electrónico"
              className="input input-bordered"
              value={email}
              onChange={(event) => setEmail(event.target.value)}
            />
            <label className="label">
              <span className="label-text">Escribe tu reporte</span>
            </label>
            <textarea
              placeholder="Mensaje"
              className="input input-bordered"
              value={message}
              onChange={(event) => setMessage(event.target.value)}
              rows="5"
              style={{ height: "200px" }}
            ></textarea>

            <div className="mt-4">
            <button className="btn bg-blue-900">
                {isSent ? "Enviado" : "Enviar Reporte"}
              </button>
              {isSent && <p className="text-green-500">El correo se ha enviado correctamente.</p>}
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Support;
