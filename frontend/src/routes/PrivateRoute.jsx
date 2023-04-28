import { Navigate } from "react-router-dom";

export const PrivateRoute = ({ children }) => {
  const currentUser = true; //cambiar a false para probar que no se podra ingrezar a la vista /chat si no se registra. esto es una prueba aun

  if(!currentUser)
  {
    return <Navigate to="/" replace={true}/>
  }
  return children;
};
