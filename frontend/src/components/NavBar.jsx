import { useRef } from "react";
import { FaBars, FaTimes } from "react-icons/fa";

function Navbar() {
  const navRef = useRef();

  const showNavbar = () => {
    navRef.current.classList.toggle("translate-y-full");
  };

  const menuOptions = [
    { id: 1, label: "Home", href: "/chat" },
    { id: 2, label: "History", href: "/history" },
    { id: 3, label: "Support", href: "/support" },
  ];

  return (
    <header className="flex items-center justify-between h-20 px-8 bg-blue-900 text-white">
      <h3 className="text-xl font-semibold">LOGO</h3>
      <nav ref={navRef} className="fixed top-0 left-0 h-screen w-screen flex flex-col items-center justify-center gap-6 bg-blue-900 transition-transform duration-500 transform -translate-y-full z-50">
        {menuOptions.map((option) => (
          <a key={option.id} href={option.href} className="text-white hover:text-red-500">
            {option.label}
          </a>
        ))}
        <button className="nav-btn nav-close-btn" onClick={showNavbar}>
          <FaTimes />
        </button>
      </nav>
      <button className="nav-btn" onClick={showNavbar}>
        <FaBars />
      </button>
    </header>
  );
}

export default Navbar;

