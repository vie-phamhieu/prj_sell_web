
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
## Tạo admin BD
```
python3 manage.py createsuperuser
```
## Chạy project
```
python3 manage.py runserver
```
### Tạo Database bằng Docker
# Tạo DB
```
docker-compose up -d
```
# Down BD (Xóa)
```
docker-compose down
```
docker ps // kiểm tra trạng thái
docker-compose down // dừng hoặc xóa
```