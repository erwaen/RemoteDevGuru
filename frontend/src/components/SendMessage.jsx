import { useState } from "react";

const SendMessage = () => {
    const [value,setvalue]=useState("");
    
    const handleSendMessage=(e)=>{
        e.preventDefault();
        console.log(value);
        setvalue("");   //limpiamos la caja de texto
    }
  return (
    <div className="bg-gray-200 fixed bottom-0 w-full py-10 shadow-lg">
      <form onSubmit={handleSendMessage} className="containerWrap flex px-3">
        <input value={value} onChange={e=>setvalue(e.target.value)} className="input w-full bg-gray-100 focus:outline-none rounded-r-none" type="text" />
        <button type="submit" className="w-auto bg-gray-500 text-white rounded-r-md px-3 text-lg">Send</button>
      </form>
    </div>
  );
};

export default SendMessage;
