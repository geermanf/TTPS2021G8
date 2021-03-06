import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { LayoutComponent } from './_layout/layout.component';

const routes: Routes = [
  {
    path: '',
    component: LayoutComponent,
    children: [
      {
        path: 'dashboard',
        loadChildren: () =>
          import('./dashboard/dashboard.module').then((m) => m.DashboardModule),
      },
      {
        path: 'user-management',
        loadChildren: () =>
          import('../modules/user-management/user-management.module').then(
            (m) => m.UserManagementModule
          ),
      },
      {
        path: 'patients',
        loadChildren: () =>
          import('../modules/patient/patient.module').then(
            (m) => m.PatientModule
          ),
      },
      {
        path: 'studies',
        loadChildren: () =>
          import('../modules/study/study.module').then(
            (m) => m.StudyModule
          ),
      },
      {
        path: 'type-studies',
        loadChildren: () =>
          import('../modules/type_study/type-study.module').then(
            (m) => m.TypeStudyModule
          ),
      },
      {
        path: '',
        redirectTo: '/dashboard',
        pathMatch: 'full',
      },
      {
        path: '**',
        redirectTo: 'error/404',
      },
    ],
  },
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule],
})
export class PagesRoutingModule { }
