import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';
import { PolicyComponent } from './policy/policy.component';
import { PoliciesComponent } from './policies/policies.component';

@NgModule({
  declarations: [
    AppComponent,
    PolicyComponent,
    PoliciesComponent
  ],
  imports: [
    BrowserModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
