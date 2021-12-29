import Header from "../components/Header";
import Footer from "../components/Footer";

function MainPage() {
    return (
        <div>
            <Header/>
            <p className="fs-1 fw-bold">Лабораторная работа №8</p>
            <p className="fs-2 fw-bold">Разработка пользовательского интерфейса с использованием библиотеки React</p>
            <p className="fs-4"><b>Цель лабораторной работы:</b> изучение возможностей создания пользовательского
                интерфейса в веб-приложениях с использованием библиотеки React.</p>

            <Footer/>
        </div>
    );
}

export default MainPage;