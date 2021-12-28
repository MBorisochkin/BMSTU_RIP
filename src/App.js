import { BrowserRouter, Routes, Route} from "react-router-dom";
import MainPage from "./pages/MainPage";

function App() {

  return (
      <BrowserRouter basename="/">
            <Routes>
                <Route path="/" element={<MainPage/>}/>
                <Route path="/new" element={ <h1>Это наша страница с чем-то новеньким</h1>}/>
            </Routes>
      </BrowserRouter>
  );
}
export default App;
