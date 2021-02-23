import { Component, OnInit } from '@angular/core';
import { CartserviceService } from '../cartservice.service';

@Component({
  selector: 'app-shipping',
  templateUrl: './shipping.component.html',
  styleUrls: ['./shipping.component.css']
})
export class ShippingComponent implements OnInit {

  constructor(
    private cartService: CartserviceService
  ) { }

  ngOnInit() {
  }
  shippingCosts = this.cartService.getShippingPrices();

}