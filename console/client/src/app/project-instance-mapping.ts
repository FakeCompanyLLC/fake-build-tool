import { ProjectInstance } from './project-instance';
import { Project } from './project';

export class ProjectInstanceMapping {
  _id: string;
  project: Project;
  instance: ProjectInstance;
  order: number;
}
