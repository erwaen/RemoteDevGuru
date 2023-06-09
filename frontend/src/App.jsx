import NavBar from "./components/NavBar";
import Login from "./pages/Login";
import Support from "./pages/Support";
import History from "./pages/History";
import ChatRoom from "./pages/ChatRoom";
import { Routes } from "react-router-dom";
import { Route } from "react-router-dom";
import { PrivateRoute } from "./routes/PrivateRoute";

function App() {
  return (
    <div>
      <Routes>
        <Route path="/history" element={<History />} />
        <Route path="/support" element={<Support />} />
        <Route path="/" element={<ChatRoom />} />
        {/* <Route
          path="/chat"
          element={
            <PrivateRoute>
              <ChatRoom />
            </PrivateRoute>
          }
        /> */}
      </Routes>
    </div>
  );
}

export default App;
