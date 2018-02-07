import { Injectable } from '@angular/core';
import { Observable } from 'rxjs/Observable';
import { BehaviorSubject } from 'rxjs/BehaviorSubject';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { Project } from './project';
import { ProjectName } from './project-name';
import { ProjectInstance } from './project-instance';
import { ProjectInstanceMapping } from './project-instance-mapping';
import { Profile } from './profile';

const httpOptions = {
  headers: new HttpHeaders({ 'Content-Type': 'application/json' }),
  withCredentials: true
};

declare var io;

@Injectable()
export class FbtService {

  socket: any;
  socketConnected$ = new BehaviorSubject<boolean>(false);
  selectedProfile: any;

  private apiUrl: string = 'api/v1/';

  constructor(
    private http: HttpClient
  ) {
    this.socket = io();
    this.socket.on('connect', () => this.socketConnected$.next(true));
    this.socket.on('disconnect', () => this.socketConnected$.next(false));

    this.socketConnected$.asObservable().subscribe( connected => {
      console.log('Socket connected: ', connected);
    });
  }

  run(profile: Profile): Observable<Profile> {
    return this.http.post<Profile>('/build/run', this.format(profile), httpOptions);
  }

  stop() {
    return this.http.get('/build/stop');
  }

  createProject(name: ProjectName): Observable<Project> {
    return this.http.post<Project>('/api/fbt/project', name);
  }

  readProject(id: string): Observable<Project> {
    return this.http.get<Project>('/api/fbt/project/' + id);
  }

  updateProject(id: string, project: Project): Observable<Project> {
    return this.http.put<Project>('/api/fbt/project/' + id, project, httpOptions);
  }

  // DELETE Project

  createProjectInstance(projectId: string, instance: ProjectInstance): Observable<ProjectInstance> {
    return this.http.post<ProjectInstance>('/api/fbt/project/' + projectId + '/instance', instance, httpOptions);
  }

  updateProjectInstance(id: String, instance: ProjectInstance): Observable<ProjectInstance> {
    return this.http.put<ProjectInstance>('/api/fbt/project/instance/' + id, instance, httpOptions);
  }

  configuration(id: string) {
    return this.http.get('/build/configuration/' + id);
  }

  updateConfiguration(configuration: any) {
    return this.http.post('/build/configuration', configuration, httpOptions)
  }

  createProfile(profile: Profile): Observable<Profile> {
    return this.http.post<Profile>('/api/fbt/profile', profile);
  }

  readProfile(id: string): Observable<Profile> {
    return this.http.get<Profile>('/api/fbt/profile/' + id);
  }

  updateProfile(id: string, profile: Profile): Observable<Profile> {
    return this.http.put<Profile>('/api/fbt/profile/' + id, profile, httpOptions);
  };

  readProjects(): Observable<Project[]> {
    return this.http.get<Project[]>('/api/fbt/projects')
  }

  readProfiles(): Observable<Profile[]> {
    return this.http.get<Profile[]>('/api/fbt/profiles')
  }

  copyProfile(id: string): Observable<Profile> {
    return this.http.post<Profile>('/api/fbt/profile/' + id + '/copy', null, httpOptions);
  }

  listen(event: string): Observable<any> {

    return new Observable(observer => {
      this.socket.on(event, data => {
        observer.next(data);
      });

      // observable is disposed
      return () => {
        this.socket.off(event);
      }

    });

  }

  format(profile: Profile): any[] {
    let projects: any[] = [];
    profile.projects.forEach((projectInstanceMapping: ProjectInstanceMapping) => {
      let project = {
        name: projectInstanceMapping.project.name.name
      };
      let instance = projectInstanceMapping.instance;
      for (var k in instance) {
        if (instance[k].length != 0 && k != 'name') {
            project[k] = instance[k];
        }
      }
      projects.push(project);
    });
    return projects;
  }

}
