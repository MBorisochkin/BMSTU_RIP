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
            <ul className="fs-4">
                {pizzas.map((pizza) => {
                    return (<li key={pizza.pk}><Link to={"/pizza/" + pizza.pk.toString()}
                                                     className="text-decoration-none link-dark">
                        {pizza.name}</Link></li>);

                })}
            </ul>
            <Footer/>
        </div>
    );
}

export default PizzaListPage;