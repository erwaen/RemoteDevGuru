import { useState } from "react";
import { FaPaperPlane } from "react-icons/fa";

const SendMessage = ({ onSend }) => {
  const [value, setValue] = useState("");
  //const [errorMessage, setErrorMessage] = useState("");

  // const handleSendMessage = async (e) => {
  //   e.preventDefault();

  //   //Si el mensaje esta vacio renderiza un aviso y retorna
  //   if (!value) {
  //     setErrorMessage("Por favor ingrese un mensaje");
  //     return;
  //   }

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
      onSend(value);
      setValue(""); //prop value is emptied
    }
  };

  // return (
  //   <div>
  //     <input
  //       type="text"
  //       placeholder="Type a message"
  //       value={text}
  //       onChange={handleChange}
  //       onKeyDown={handleKeyDown}
  //     />
  //     <button onClick={() => {
  //       onSend(text);
  //       setText('');
  //     }}>Send</button>
  //   </div>
  // );

  return (
    <div>
      <input
        type="text"
        value={value}
        onChange={handleChange}
        onKeyDown={handleKeyDown}
      />
      <button
        onClick={() => {
          onSend(value);
          setValue("");
        }}
      >
        <FaPaperPlane />
      </button>
    </div>

    // <div onSubmit={handleSendMessage} className="fixed bottom-0 left-0 right-0">
    //   <form className="flex items-center justify-between">
    //     {/* Box input */}
    //     <input
    //       type="text"
    //       className="w-full h-12 rounded-l-lg p-4 border-t mr-0 border-b border-l text-gray-800 border-gray-200 bg-gray-300"
    //       placeholder="Escribe tu mensaje..."
    //       value={value}
    //       onChange={(e) => setValue(e.target.value)}
    //     />

    //     {/* Button submit message */}
    //     <button
    //       type="submit"
    //       className="w-17 h-12 bg-blue-900 text-white rounded-r-md px-3 text-lg flex items-center justify-center"
    //     >
    //       <FaPaperPlane />
    //     </button>
    //   </form>

    //   {
    //     /*Show an error message under box input*/
    //     errorMessage && (
    //       <p className="text-red-500 text-xs italic mt-2">{errorMessage}</p>
    //     )
    //   }
    // </div>
  );
};

export default SendMessage;
