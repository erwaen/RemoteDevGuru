const Login = () => {
  return (
    <div className="hero min-h-screen bg-base-200">
      <div className="hero-content text-center">
        <div className="max-w-md mx-auto">
          <h1 className="text-3xl md:text-5xl font-bold">Bienvenido al Remote Dev Guru</h1>
          <p className="py-4">
            Para comenzar a chatear, inicie sesión
          </p>
          <div className="flex flex-col gap-4">
            <button className="btn">Continuar con Google</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Login;

