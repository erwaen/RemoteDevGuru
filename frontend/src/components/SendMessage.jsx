import { useState } from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faPaperPlane } from "@fortawesome/free-solid-svg-icons";

const SendMessage = ({ onSendMessage }) => {
  const [value, setValue] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  const handleSendMessage = async (e) => {
    e.preventDefault();
    if (!value) {
      setErrorMessage("Por favor ingrese un mensaje");
      return;
    }

    try {
      const apiKey = "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";
      const endpoint = `https://api.openai.com/v1/completions`;

      const response = await fetch(endpoint, {
        method: "POST",
        headers: {
          "Content-Type": `application/json`,
          Authorization: `Bearer ${apiKey}`,
        },
        body: JSON.stringify({
          prompt: value,
          temperature: 0.5,
          model: "text-ada-001",
        }),
      });

      const data = await response.json();

      if (data.choices && data.choices.length > 0) {
        const generatedText = data.choices[0].text;
        onSendMessage(generatedText);
      }

      setErrorMessage("");
      setValue("");
    } catch (error) {
      console.error(error);
      setErrorMessage("Error al enviar el mensaje");
    }
  };

  return (
    <div onSubmit={handleSendMessage} className="fixed bottom-0 left-0 right-0">
    <form className="flex items-center justify-between">
        <input
          type="text"
          className="w-full rounded-l-lg p-4 border-t mr-0 border-b border-l text-gray-800 border-gray-200 bg-white"
          placeholder="Escribe tu mensaje..."
          value={value}
          onChange={(e) => setValue(e.target.value)}
        />
        <button
          type="submit"
          className="w-20 h-10 bg-gray-500 text-white rounded-r-md px-3 text-lg flex items-center justify-center"
        >
          <FontAwesomeIcon icon={faPaperPlane} />
        </button>
      </form>
      {errorMessage && (
        <p className="text-red-500 text-xs italic mt-2">{errorMessage}</p>
      )}
    </div>
  );
};

export default SendMessage;
