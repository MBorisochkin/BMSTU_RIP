export class PizzaComponent {
    constructor(parent) {
        this.parent = parent;
    }

    getHTML(data) {
        return (`
        <div class="card mb-3" style="width: 540px;">
                    <div class="row g-0">
                        <div class="col-md-4">
                            <img src="https://www.maggi.ru/data/images/recept/img640x618/recept_3585_j66m.jpg" 
                            class="img-fluid" alt="Сегодня без пиццы :("/>
                        </div>
                        <div class="col-md-8">
                            <div class="card-body">
                                <h5 class="card-title">${data.name}</h5>
                                <p class="card-subtitle">Состав:</p>
                                <p class="card-text">${data.topping}</p>
                                <p class="card-subtitle">Диаметр:</p>
                                <p class="card-text">${data.diameter}</p>
                            </div>
                        </div>
                    </div>
                </div>
        `);
    }

    render(data) {
        const html = this.getHTML(data);
        this.parent.insertAdjacentHTML('beforeend', html);
    }
}
