import { FaBars, FaTimes } from "react-icons/fa";
import { useState } from "react";
import { Link } from "react-router-dom";
import icon from "../assets/3.png";

const Navbar = () => {
  const [openMenu, setOpenMenu] = useState(false);

  return (
    <div className="z-10 shadow-md w-full py-4 justify-between top-0 fixed bg-zinc-900 left-0 md:flex">
      <div className="flex font-bold text-gray-200 text-xl ml-7 items-center">
        <img src={icon} alt="" className="w-8" />
        <a className="ml-1">RemoteDevGuru</a>
      </div>
      <div
        onClick={() => setOpenMenu(!openMenu)}
        className="text-gray-200 text-xl absolute right-6 top-5 cursor-pointer md:hidden"
      >
        {openMenu ? <FaTimes /> : <FaBars />}
      </div>
      <ul
        className={`md:flex md:items-center text-lg md:pb-0 pb-4 md:static absolute bg-zinc-900 md:z-auto z-10 md:w-auto w-full transition-all duration-500 ease-in ${
          openMenu
            ? "top-[61px] opacity-100"
            : "top-[-130px] md:opacity-100 opacity-0"
        }`}
      >
        <li className="text-gray-200 hover:text-gray-400 duration-300 md:mr-8 md:my-0 my-5 text-center">
          <Link to="/">Chat</Link>
        </li>
        <li className="text-gray-200 hover:text-gray-400 duration-300 md:mr-10 text-center">
          <Link to="/support">Support</Link>
        </li>
      </ul>
    </div>
  );
};

export default Navbar;