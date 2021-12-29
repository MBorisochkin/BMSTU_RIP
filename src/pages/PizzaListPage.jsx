import React, {useEffect, useState} from "react";
import {Link} from "react-router-dom";
import Header from "../components/Header";
import Footer from "../components/Footer";
import GetPizzas from "../modules/GetPizzas";

function PizzaListPage() {

    const [pizzas, setPizzas] = useState([]);

    const handlePizzasList = async () => {
        const results = await GetPizzas();
        await setPizzas(results);
    }

    useEffect(() => {
        handlePizzasList();
    }, []);

    return (
        <div>
            <Header/>
            <ul className="fs-5 ">
                {pizzas.map((pizza) => {
                    return (<li key={pizza.pk}><Link to="pizza/:pk" className="text-decoration-none link-dark">
                        {pizza.name}</Link></li>);
                    // {location => `pizza/${pizza.pk}`}
                })}
            </ul>
            <Footer/>
        </div>
    );
}

export default PizzaListPage;