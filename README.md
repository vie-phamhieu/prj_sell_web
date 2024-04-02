## Tạo Database bằng Docker
```
docker-compose up -d
docker ps // kiểm tra trạng thái
docker-compose down // dừng hoặc xóa
```
## Cài đặt python django
```
python install django
```
## Start project
```
django-admin startproject <project name>
```
## Start new app
```
django-admin startapp <app name>
```
## Lưu thay đổi trong DB
```
python3 manage.py migrate
```
## Chạy project
```
python3 manage.py runserver
```
