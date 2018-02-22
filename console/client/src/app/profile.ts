import { ProjectInstanceMapping } from './project-instance-mapping';

export class Profile {
  _id: string;
  name: string;
  projects: ProjectInstanceMapping[];
}
