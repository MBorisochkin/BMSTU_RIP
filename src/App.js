import { BrowserRouter, Routes, Route} from "react-router-dom";
import MainPage from "./pages/MainPage";
import PizzaListPage from "./pages/PizzaListPage";

function App() {

  return (
      <BrowserRouter basename="/">
            <Routes>
                <Route path="/" element={<MainPage/>}/>
                <Route path="/pizza" element={<PizzaListPage/>}/>
            </Routes>
      </BrowserRouter>
  );
}
export default App;
