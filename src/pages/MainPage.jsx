import Header from "../components/Header";
import Footer from "../components/Footer";

function MainPage() {
    return (
        <div>
            <Header/>
            <h1 className="ms-3">Это наша стартовая страница</h1>
            <Footer/>
        </div>
    );
}

export default MainPage;