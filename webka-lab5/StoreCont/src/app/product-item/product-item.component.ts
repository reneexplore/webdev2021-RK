import { Component, OnInit } from '@angular/core';
import { products } from "../products";
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-product-item',
  templateUrl: './product-item.component.html',
  styleUrls: ['./product-item.component.css']
})
export class ProductItemComponent implements OnInit {

  products = products;
  category_id;

  constructor(
    private route: ActivatedRoute

  ) { }

  ngOnInit() {
    const routeParams = this.route.snapshot.paramMap;
    const categoryIdRoute = Number(routeParams.get('categoriesId'));
    this.category_id =  categoryIdRoute;

 }
 likeItem(id_uniq) {
  products[id_uniq].likes+=1
}
removeItem(id_uniq) {
  products.splice(id_uniq, 1)
  for (var i=id_uniq; i<products.length; i++) {
    products[i].id_uniq = i
  }
}

}
