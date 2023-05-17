import { useState } from "react";
import { FaPaperPlane } from "react-icons/fa";

const SendMessage = ({ onSend }) => {
  const [value, setValue] = useState("");
  const [errorMessage, setErrorMessage] = useState("");

  // const handleSendMessage = async (e) => {
  //   e.preventDefault();

  //   try {
  //     const endpoint = `http://localhost:8001/api/chat/user_message`;
  //     const response = await fetch(endpoint, {
  //       method: "POST",
  //       headers: {
  //         "Content-Type": `application/json`,
  //       },
  //       body: JSON.stringify({
  //         message: value,
  //       }),
  //     });
  //     console.log(response);

  //     const data = await response.json();
  //     console.log(data);
  //     //const apiKey = "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";
  //     //const endpoint = `https://api.openai.com/v1/completions`;

  //     // const response = await fetch(endpoint, {
  //     //   method: "POST",
  //     //   headers: {
  //     //     "Content-Type": `application/json`,
  //     //     Authorization: `Bearer ${apiKey}`,
  //     //   },
  //     //   body: JSON.stringify({
  //     //     prompt: value,
  //     //     temperature: 0.5,
  //     //     model: "text-davinci-003",
  //     //   }),
  //     // });

  //     // const data = await response.json();
  //     // console.log(data);

  //     // if (data.choices && data.choices.length > 0) {
  //     //   const generatedText = data.choices[0].text;
  //     //   onSendMessage(generatedText);
  //     // }

  //     setErrorMessage("");
  //     setValue("");
  //   } catch (error) {
  //     console.error(error);
  //     setErrorMessage("Error al enviar el mensaje");
  //   }
  // };

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