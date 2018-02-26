import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HttpClientModule, HttpClient } from '@angular/common/http';
import {
  MatAutocompleteModule,
  MatButtonModule,
  MatButtonToggleModule,
  MatCardModule,
  MatCheckboxModule,
  MatChipsModule,
  MatDatepickerModule,
  MatDialogModule,
  MatExpansionModule,
  MatGridListModule,
  MatIconModule,
  MatInputModule,
  MatListModule,
  MatMenuModule,
  MatNativeDateModule,
  MatPaginatorModule,
  MatProgressBarModule,
  MatProgressSpinnerModule,
  MatRadioModule,
  MatRippleModule,
  MatSelectModule,
  MatSidenavModule,
  MatSliderModule,
  MatSlideToggleModule,
  MatSnackBarModule,
  MatSortModule,
  MatTableModule,
  MatTabsModule,
  MatToolbarModule,
  MatTooltipModule,
  MatStepperModule,
} from '@angular/material';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { CdkTableModule } from '@angular/cdk/table';
import { FbtService } from './fbt.service';
import { HomeComponent } from './home/home.component';
import { ProjectComponent } from './project/project.component';
import { ProfileComponent } from './profile/profile.component';
import { ProjectSetupComponent } from './project-setup/project-setup.component';
import { ProjectInstanceComponent } from './project-instance/project-instance.component';
import { ProfileSetupComponent } from './profile-setup/profile-setup.component';
import { ProfileStatusComponent, StartBuildComponent } from './profile-status/profile-status.component';
import { ProjectSelectorComponent } from './project-selector/project-selector.component';
import { ProjectListComponent, ProjectAddComponent } from './project-list/project-list.component';
import { ProfileListComponent, ProfileAddComponent } from './profile-list/profile-list.component';

@NgModule({
  imports: [
    FormsModule,
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    CdkTableModule,
    MatAutocompleteModule,
    MatButtonModule,
    MatButtonToggleModule,
    MatCardModule,
    MatCheckboxModule,
    MatChipsModule,
    MatStepperModule,
    MatDatepickerModule,
    MatDialogModule,
    MatExpansionModule,
    MatGridListModule,
    MatIconModule,
    MatInputModule,
    MatListModule,
    MatMenuModule,
    MatNativeDateModule,
    MatPaginatorModule,
    MatProgressBarModule,
    MatProgressSpinnerModule,
    MatRadioModule,
    MatRippleModule,
    MatSelectModule,
    MatSidenavModule,
    MatSliderModule,
    MatSlideToggleModule,
    MatSnackBarModule,
    MatSortModule,
    MatTableModule,
    MatTabsModule,
    MatToolbarModule,
    MatTooltipModule,
    HttpClientModule
  ],
  entryComponents: [AppComponent, StartBuildComponent, ProfileAddComponent, ProjectSelectorComponent, ProjectAddComponent, ProjectInstanceComponent],
  declarations: [
    AppComponent,
    StartBuildComponent,
    ProfileAddComponent,
    HomeComponent,
    ProjectComponent,
    ProfileComponent,
    ProjectSetupComponent,
    ProfileSetupComponent,
    ProfileStatusComponent,
    ProjectSelectorComponent,
    ProjectListComponent,
    ProfileListComponent,
    ProjectAddComponent,
    ProjectInstanceComponent
  ],
  providers: [FbtService],
  bootstrap: [AppComponent]
})
export class AppModule { }
