import { TestBed, inject } from '@angular/core/testing';

import { FbtService } from './fbt.service';

describe('FbtService', () => {
  beforeEach(() => {
    TestBed.configureTestingModule({
      providers: [FbtService]
    });
  });

  it('should be created', inject([FbtService], (service: FbtService) => {
    expect(service).toBeTruthy();
  }));
});
