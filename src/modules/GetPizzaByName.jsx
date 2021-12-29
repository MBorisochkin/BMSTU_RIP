const GetPizzaByName = async (name='') => {
    return await fetch(`http://localhost:8000/pizza/${name}`, {method: "GET"})
        .then((response) => {
            return response.json();
        }).catch(() => {
            return {resultCount: 0, results: []};
        });
}

export default GetPizzaByName;