import React, { useState } from 'react';
import { Link } from 'react-router-dom';

const NavBar = () => {
  const [isMenuOpen, setMenuOpen] = useState(false);

  const toggleMenu = () => {
    setMenuOpen(!isMenuOpen);
  };

  const menuOptions = [
    { id: 1, label: 'Home', href: '/chat' },
    { id: 2, label: 'History', href: '/history' },
    { id: 3, label: 'Support', href: '/support' },
  ];

  return (
    <div className="navbar bg-neutral text-neutral-content">
      <div className="containerWrap flex justify-between">
        <button
          className="menu-btn flex items-center justify-center p-1 rounded-md focus:outline-none bg-white"
          onClick={toggleMenu}
        >
          <span
            className={`menu-icon h-0.5 w-4 bg-neutral transition-transform duration-300 ${
              isMenuOpen ? 'transform rotate-45' : ''
            }`}
          ></span>
          <span
            className={`menu-icon h-0.5 w-4 bg-neutral transition-opacity duration-300 ${
              isMenuOpen ? 'opacity-0' : ''
            }`}
          ></span>
          <span
            className={`menu-icon h-0.5 w-4 bg-neutral transition-transform duration-300 ${
              isMenuOpen ? 'transform -rotate-45' : ''
            }`}
          ></span>
        </button>
        <Link to="/" className="btn btn-ghost normal-case text-xl">
          Remote Dev Guru
        </Link>
        <button>Logout</button>
      </div>
      {isMenuOpen && (
        <div className="menu-dropdown mt-2 bg-transparent border border-white">
          <div className="flex flex-row-reverse">
            {menuOptions.map((option) => (
              <Link
                key={option.id}
                to={option.href}
                className="block py-2 px-4 text-white hover:text-gray-300 border-t border-white"
              >
                {option.label}
              </Link>
            ))}
          </div>
        </div>
      )}
    </div>
  );
};

export default NavBar;
