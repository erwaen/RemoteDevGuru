const NavBar = () => {
  return (
    <div className="navbar bg-neutral text-neutral-content">
      <div className="containerWrap flex justify-between">
        <a className="btn btn-ghost normal-case text-xl">Remote Dev Guru</a>
        <button>Logout</button>
      </div>
    </div>
  );
};

export default NavBar;
