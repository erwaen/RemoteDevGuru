import { useState } from "react";
import { FaPaperPlane } from "react-icons/fa";

const SendMessage = ({ onSend }) => {
  const [value, setValue] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  //set value on prop value
  const handleChange = (e) => {
    setValue(e.target.value);
  };

  //set value on prop value when Enter is presionated
  const handleKeyDown = (e) => {
    if (e.key == "Enter") {
      handleSendMessage();
    }
  };

  //call onSend
  const handleSendMessage = () => {
    //if value is empty show a warning
    if (value == "") {
      setErrorMessage("Por favor, Escriba un mensaje...");
      return;
    }
    onSend(value);
    setValue(""); //prop value is emptied
    setErrorMessage(""); //prop ErrorMessage is emptied
  };

  return (
    <div className="fixed bottom-3 left-7 right-7 items-center">
      <div className="flex justify-between">
        {/* Box input */}
        <input
          type="text"
          className="w-full h-12 bg-gray-300 rounded-l-lg ps-5"
          value={value}
          placeholder="Escribe algo..."
          onChange={handleChange}
          onKeyDown={handleKeyDown}
        />

        {/* Button submit message */}
        <button
          className="flex w-20 h-12 rounded-r-lg items-center justify-center bg-zinc-800"
          onClick={handleSendMessage}
        >
          <FaPaperPlane style={{ color: "#ffffff" }} />
        </button>
      </div>

      {/*Show an error message under box input*/}
      <p className="text-red-500 text-xs italic mt-2">{errorMessage}</p>
    </div>
  );
};

export default SendMessage;
