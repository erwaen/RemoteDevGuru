import React, { useState } from "react";

const Support = () => {
  const [name, setName] = useState("");
  const [lastName, setLastName] = useState("");
  const [message, setMessage] = useState("");

  const handleSubmit = (event) => {
    event.preventDefault();
    console.log(`Nombre: ${name}, Apellido: ${lastName}`);
  };

  return (
    <div className="hero min-h-screen bg-base-100">
      <div className="hero-content text-center">
        <div className="max-w-md mx-auto">
          <h1 className="text-3xl md:text-5xl font-bold mb-10">Bienvenido a Soporte</h1>
          <form onSubmit={handleSubmit} className="flex flex-col gap-0.5">
            <label className="label">
              <span className="label-text">Cual es tu nombre?</span>
            </label>
            <input
              type="text"
              placeholder="Nombre"
              className="input input-bordered"
              value={name}
              onChange={(event) => setName(event.target.value)}
            />
            <label className="label">
              <span className="label-text">Cual es tu apellido?</span>
            </label>
            <input
              type="text"
              placeholder="Apellido"
              className="input input-bordered"
              value={lastName}
              onChange={(event) => setLastName(event.target.value)}
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
              <button type="submit" className="btn">
                Enviar Reporte
              </button>
            </div>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Support;


