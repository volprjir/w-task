import {Component, OnInit} from '@angular/core';
import {StoreService} from './services/store.service';
import {debounceTime, distinctUntilChanged, map, startWith} from 'rxjs/operators';
import {Observable, Subject, Subscription} from 'rxjs';
import {FormControl} from '@angular/forms';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit {
  control = new FormControl();
  toSearch = '';
  results: any;
  suggestion = [];
  filteredStores: Observable<string[]>;
  private storesModelChanged: Subject<string> = new Subject<string>();
  private storesModelChangeSubscription: Subscription;


  constructor(private storeService: StoreService) {
    this.storesModelChangeSubscription = this.storesModelChanged
      .pipe(
        debounceTime(100),
        distinctUntilChanged()
      )
      .subscribe(newText => {
        this.getData();
      });

    this.getData(true);
  }

  getData(init: boolean = false) {
    const toSearch = this.toSearch.length > 1 ? this.toSearch : '';
    this.storeService.fetchResults(toSearch).pipe(
      map(res => res[`results`])
    ).subscribe(
      res => {
        this.results = res;
        if (init) {
          this.results.forEach(item => {
            this.suggestion.push(item["name"]);
            this.suggestion.push(item["postcode"]);
          });
        }
        console.log('result', this.results);
      }
    );
  }

  ngOnInit() {
    this.filteredStores = this.control.valueChanges.pipe(
      startWith(''),
      map(value => this._filter(value))
    );
  }

  private _filter(value: string): string[] {
    const filterValue = this._normalizeValue(value);
    return this.suggestion.filter(store => this._normalizeValue(store).includes(filterValue));
  }

  private _normalizeValue(value: string): string {
    return value.toLowerCase().replace(/\s/g, '');
  }

  onFieldChanged(toFind) {
    this.storesModelChanged.next(toFind);
  }
}
