import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
@Injectable({
  providedIn: 'root'
})
export class CartserviceService {
   items = [];
   addToCart(product) {
    this.items.push(product);
  }

  getItems() {
    return this.items;
  }

  clearCart() {
    this.items = [];
    return this.items;
  }
  constructor(
      private http: HttpClient
  ) { }
  getShippingPrices() {
    return this.http.get('/assets/shipping.json');
  }

}
