import React, { useState } from "react";
import { Input, Textarea } from "daisyui";

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
        <div className="max-w-md">
          <h1 className="text-5xl font-bold">Bienvenido a Soporte</h1>
          <form onSubmit={handleSubmit}>
            <div className="form-control w-full max-w-xs">
              <label className="label">
                <span className="label-text">Cual es tu nombre?</span>
              </label>
              <input
                type="text"
                placeholder="Nombre"
                className="input input-bordered w-full max-w-xs"
                value={name}
                onChange={(event) => setName(event.target.value)}
              />
              <label className="label">
                <span className="label-text">Cual es tu apellido?</span>
              </label>
              <input
                type="text"
                placeholder="Apellido"
                className="input input-bordered w-full max-w-xs"
                value={lastName}
                onChange={(event) => setLastName(event.target.value)}
              />
<label className="label">
  <span className="label-text">Escribe tu reporte</span>
</label>
<textarea
  placeholder="Mensaje"
  className="input input-bordered w-full max-w-xs"
  value={message}
  onChange={(event) => setLastMessage(event.target.value)}
  rows="5"
  style={{ height: "200px", width: "100%" }}
></textarea>

            </div>
            
            <button type="submit" className="btn">
              Enviar Reporte
            </button>
          </form>
        </div>
      </div>
    </div>
  );
};

export default Support;

