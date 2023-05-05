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
        <div className="max-w-md">
          <h1 className="text-5xl font-bold">Historial de Conversaciones</h1>
          <p className="py-6">
          </p>
          <Button text="Historial 1" />
          <Button text="Historial 2" />
          <Button text="Historial 3" />
          <Button text="Historial 4" />
          <Button text="Historial 5" />
        </div>
      </div>
    </div>
  );
};

export default History;
