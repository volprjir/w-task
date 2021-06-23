import { Injectable } from '@angular/core';
import {HttpClient} from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class StoreService {

  constructor(private http: HttpClient) { }

  fetchResults(substr: string) {
    const url = substr ? `http://localhost:8888/filter?find=${substr}` : `http://localhost:8888/filter`;
    return this.http.get(url);
  }
}
