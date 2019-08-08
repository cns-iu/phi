import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { CNSPubVisModule } from 'cns-pubvis';
import { MarkdownModule } from 'ngx-markdown';

import { AppComponent } from './app.component';


@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    CNSPubVisModule,
    MarkdownModule.forRoot()
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
