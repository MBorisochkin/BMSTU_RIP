export class PizzaCardComponent {
    constructor(parent) {
        this.parent = parent;
    }

    getHTML(data) {
        return (
            `<div class="card" style="width: 300px;">
                    <img class="card-img-top" 
                        src="https://www.maggi.ru/data/images/recept/img640x618/recept_3585_j66m.jpg" 
                        alt="Сегодня без пиццы :("
                    />
                    <div class="card-body">
                        <h5 class="card-title">${data.name}</h5>
                        <p class="card-text">${data.topping}</p>
                        <button class="btn btn-primary" id="click-card-${data.pk}" data-id="${data.pk}">
                            Подробнее
                        </button>
                    </div>
                </div>`
        )
    }

    addListeners(data, listener) {
        document
            .getElementById(`click-card-${data.pk}`)
            .addEventListener("click", listener);
    }

    render(data, listener) {
        const html = this.getHTML(data);
        this.parent.insertAdjacentHTML('beforeend', html);
        this.addListeners(data, listener);
    }
}
