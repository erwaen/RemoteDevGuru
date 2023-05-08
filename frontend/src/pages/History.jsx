import React from "react";

const Button = ({ text }) => {
  return (
    <button className="btn">{text}</button>
  );
};

const History = () => {
  return (
    <div className="hero min-h-screen bg-base-200">
      <div className="hero-content text-center">
        <div className="max-w-md mx-auto">
          <h1 className="text-3xl md:text-5xl font-bold mb-10">Historial de Conversaciones</h1> {/* Se agregó mb-6 para separar el título de los botones */}
          <div className="flex flex-col gap-4">
            <Button text="Historial 1" />
            <Button text="Historial 2" />
            <Button text="Historial 3" />
            <Button text="Historial 4" />
            <Button text="Historial 5" />
          </div>
        </div>
      </div>
    </div>
  );
};

export default History;

