const GetPizzas = async () => {
    return await fetch(`http://localhost:8000/pizza/`, {method: "GET"})
        .then((response) => {
            return response.json();
        }).catch(() => {
            return {resultCount: 0, results: []};
        });
}

export default GetPizzas;