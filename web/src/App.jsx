import { createBrowserRouter } from "react-router-dom";
import Dashboard from "./components/Dashboard";
import "./App.scss";

const App = createBrowserRouter([
  {
    path: "/",
    element: <div>Корень!</div>,
  },
  {
    path: "/dashboard",
    element: <Dashboard />,
  },
]);

export default App;
