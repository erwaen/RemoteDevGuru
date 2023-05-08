import { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPaperPlane } from "@fortawesome/free-solid-svg-icons";

const SendMessage = () => {
  const [value, setValue] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const handleSendMessage = (e) => {
    e.preventDefault();
    if (!value) {
      setErrorMessage("Por favor ingrese un mensaje");
      return;
    }
    console.log(value);
    setErrorMessage("");
    setValue(""); //limpiamos la caja de texto
  };

  return (
    <div className="bg-1E1E1E fixed bottom-0 w-full py-10 shadow-lg">
      <form onSubmit={handleSendMessage} className="containerWrap px-3 flex items-center">
        <input
          value={value}
          onChange={(e) => setValue(e.target.value)}
          className="input flex-1 bg-gray-100 focus:outline-none rounded-r-none text-black mr-2"
          type="text"
          placeholder="Escribe un mensaje"
        />

        <button
          type="submit"
          className="w-20 h-10 bg-gray-500 text-white rounded-r-md px-3 text-lg flex items-center justify-center"
        >
          <FontAwesomeIcon icon={faPaperPlane} />
        </button>
      </form>
      {errorMessage && (
        <p className="text-red-500 text-sm italic ml-3">{errorMessage}</p>
      )}
    </div>
  );
};

export default SendMessage;

