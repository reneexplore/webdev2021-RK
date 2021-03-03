import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { ReactiveFormsModule } from '@angular/forms';

import { AppComponent } from './app.component';

import { ProductListComponent } from './product-list/product-list.component';

import { ProductItemComponent } from './product-item/product-item.component';


@NgModule({
  imports: [
    BrowserModule,

    ReactiveFormsModule,
    ReactiveFormsModule,
    RouterModule.forRoot([
      { path: '', component: ProductListComponent  },
      { path: 'categories/:categoriesId', component: ProductItemComponent },

    ])
  ],
  declarations: [
    AppComponent,
    ProductListComponent,
    ProductItemComponent
  ],
  bootstrap: [
    AppComponent
  ]
})
export class AppModule { }


/*
Copyright Google LLC. All Rights Reserved.
Use of this source code is governed by an MIT-style license that
can be found in the LICENSE file at https://angular.io/license
*/
