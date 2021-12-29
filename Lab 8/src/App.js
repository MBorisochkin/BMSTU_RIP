import { BrowserRouter, Routes, Route} from "react-router-dom";
import MainPage from "./pages/MainPage";
import PizzaListPage from "./pages/PizzaListPage";
import PizzaDetailPage from "./pages/PizzaDetailPage";

function App() {

  return (
      <BrowserRouter basename="/">
            <Routes>
                <Route path="/" element={<MainPage/>}/>
                <Route path="/pizza" element={<PizzaListPage/>}/>
                <Route path="/pizza/:pk" element={<PizzaDetailPage/>}/>
            </Routes>
      </BrowserRouter>
  );
}
export default App;
