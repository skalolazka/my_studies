#!/usr/bin/perl

use strict;
use warnings;

package MyQueue;

sub new {
    my ($class, $capacity) = @_;
    return unless defined($capacity); # let us have no defaults
    my $self = { values => [map {undef} (0..$capacity-1)], start => 0, end => 0, empty => 1 };
    # 'tis funny, but in perl's (0..$x) $x is included
    return bless $self => $class;
}

sub resize {
    my $self = shift;
    my $len = scalar(@{$self->{values}});
    $self->{values} = [@{$self->{values}}, map {undef} (0..$len-1)];
    # well, I have read in a cool article that it's the common practice - to double the size in resizing
    if ($self->{start}) {
        for (my $i = $self->{start}; $i < $len; $i++) {
            $self->{values}[$i+$len] = $self->{values}[$i];
        }
        $self->{start} += $len;
    }
}

sub enqueue {
    my ($self, $value) = @_;
    if (!$self->{empty} && ($self->{end} == $self->{start} || ($self->{start} == 0 && $self->{end} == scalar(@{$self->{values}})))) {
        $self->resize();
    }
    if ($self->{end} == scalar(@{$self->{values}})) {
        $self->{end} = 0;
    }
    $self->{empty} = 0;
    $self->{values}[$self->{end}] = $value;
    $self->{end}++;
}

sub dequeue {
    my $self = shift;
    my $elem = undef;
    unless ($self->{empty}) {
        $elem = $self->{values}[$self->{start}];
        if ($self->{start} == scalar(@{$self->{values}}) - 1) {
            $self->{start} = 0;
        }
        else {
            $self->{start}++;
        }
    }
    if ($self->{start} == $self->{end}) {
        $self->{empty} = 1;
    }
    return $elem;
}

sub size {
    my $self = shift;
    if ($self->{end} >= $self->{start}) {
        return $self->{end} - $self->{start}
    }
    else {
        return $self->{end} + (scalar(@{$self->{values}}) - $self->{start});
    }
}

package TestMyQueue;

use Test::More;
use Test::Deep;

my $q = MyQueue->new(5); # 5 - capacity
is_deeply($q, {'values' => [map {undef} (1..5)], end => 0, start => 0, empty => 1}, 'created with capacity 5');
$q = MyQueue->new(2); # 2 - capacity
is_deeply($q, {'values' => [undef, undef], end => 0, start => 0, empty => 1}, 'created with capacity 2');
is($q->size(), 0, 'size 0 after init');
$q->enqueue(4);
is_deeply($q, {'values' => [4,undef], 'end' => 1, 'start' => 0, empty => 0}, 'enqueue once');
is($q->size(), 1, 'size 1');
$q->enqueue(5);
is_deeply($q, {'values' => [4,5], 'end' => 2, 'start' => 0, empty => 0}, 'enqueue again');
is($q->size(), 2, 'size 2');
$q->enqueue(6);
is_deeply($q, {'values' => [4,5,6,undef], 'end' => 3, 'start' => 0, empty => 0}, 'enqueue third time - resize');
is($q->size(), 3, 'size 3');
is($q->dequeue(), 4, 'dequeue');
is_deeply($q, {'values' => [4,5,6,undef], 'end' => 3, 'start' => 1, empty => 0}, 'after dequeue');
is($q->size(), 2, 'size changed after dequeue');
$q->enqueue(7);
is_deeply($q, {'values' => [4,5,6,7], 'end' => 4, 'start' => 1, empty => 0}, 'enqueue more');
is($q->dequeue(), 5, 'dequeue 5');
is_deeply($q, {'values' => [4,5,6,7], 'end' => 4, 'start' => 2, empty => 0}, 'after dequeue');
$q->enqueue(8);
is_deeply($q, {'values' => [8,5,6,7], 'end' => 1, 'start' => 2, empty => 0}, 'enqueue again');
is($q->dequeue(), 6, 'dequeue again');
is($q->dequeue(), 7, 'dequeue again and again');
is_deeply($q, {'values' => [8,5,6,7], 'end' => 1, 'start' => 0, empty => 0}, 'after dequeues');
is($q->dequeue(), 8, 'dequeue takes it from start now');
is_deeply($q, {'values' => [8,5,6,7], 'end' => 1, 'start' => 1, empty => 1}, 'after dequeue - empty');
is($q->dequeue(), undef, 'nothing to dequeue');
is($q->dequeue(), undef, 'still nothing to dequeue');
is($q->size(), 0, 'size 0 again');
$q->enqueue(9);
is_deeply($q, {'values' => [8,9,6,7], 'end' => 2, 'start' => 1, empty => 0}, 'added one value');
$q->enqueue(10);
is_deeply($q, {'values' => [8,9,10,7], 'end' => 3, 'start' => 1, empty => 0}, 'added one more value');
$q->enqueue(11);
is_deeply($q, {'values' => [8,9,10,11], 'end' => 4, 'start' => 1, empty => 0}, 'added another value');
$q->enqueue(12);
is_deeply($q, {'values' => [12,9,10,11], 'end' => 1, 'start' => 1, empty => 0}, 'and added another value');
$q->enqueue(13);
is_deeply($q, {'values' => [12,13,10,11,undef,9,10,11], 'end' => 2, 'start' => 5, empty => 0}, 'and resize now!');
is($q->size, 5, 'size after resize');
is($q->dequeue(), 9, 'dequeue after resize');
is_deeply($q, {'values' => [12,13,10,11,undef,9,10,11], 'end' => 2, 'start' => 6, empty => 0}, 'and resize now!');
is($q->size, 4, 'size after resize and dequeue');

done_testing;
