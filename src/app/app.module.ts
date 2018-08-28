import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';

import { AppComponent } from './app.component';

import { CNSPubVisModule } from 'cns-pubvis';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    CNSPubVisModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
