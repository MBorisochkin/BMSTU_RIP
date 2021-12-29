const GetPizzaByPK = async (pk = 0) => {
    return await fetch(`http://localhost:8000/pizza/${pk}/`, {method: "GET"})
        .then((response) => {
            return response.json();
        }).catch(() => {
            return {resultCount: 0, results: []};
        });
}

export default GetPizzaByPK;