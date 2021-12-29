import React, {useEffect, useState} from "react";
import {useParams} from "react-router";
import {Table} from "react-bootstrap";
import Header from "../components/Header";
import Footer from "../components/Footer";
import GetPizzaByPK from "../modules/GetPizzaByPK";

function PizzaDetailPage() {
    const pk = useParams().pk;
    console.log(pk);
    
    const [pizza, setPizza] = useState({});

    const handlePizza = async () => {
        const result = await GetPizzaByPK(pk);
        await setPizza(result);
    }

    useEffect(() => {
        handlePizza();}, []);

    useEffect(() => {
        console.log(pizza);}, [pizza])

    return (
        <div>
            <Header/>
            <Table striped bordered size="sm" className="fs-4">
                <tbody>
                <tr>
                    <td className="mx-2">Название</td>
                    <td className="mx-2">{pizza.name}</td>
                </tr>
                <tr>
                    <td className="mx-2">Состав</td>
                    <td className="mx-2">{pizza.topping}</td>
                </tr>
                <tr>
                    <td className="mx-2">Диаметр</td>
                    <td className="mx-2">{pizza.diameter}</td>
                </tr>
                </tbody>
            </Table>
            <Footer/>
        </div>
    );
}

export default PizzaDetailPage;